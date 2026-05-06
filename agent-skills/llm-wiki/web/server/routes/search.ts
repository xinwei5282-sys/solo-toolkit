import fs from "node:fs";
import path from "node:path";
import type { Request, Response } from "express";
import type { ServerConfig } from "../config.js";

interface SearchHit {
  path: string;
  title: string;
  snippet: string;
}

function walkMd(dir: string, root: string): string[] {
  const results: string[] = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...walkMd(full, root));
    } else if (entry.name.endsWith(".md")) {
      results.push(full);
    }
  }
  return results;
}

function extractTitle(content: string, filePath: string): string {
  const m = content.match(/^#\s+(.+)$/m);
  if (m) return m[1]!.trim();
  return path.basename(filePath, ".md").replace(/-/g, " ");
}

function buildSnippet(content: string, query: string): string {
  const lower = content.toLowerCase();
  const qLower = query.toLowerCase();
  const idx = lower.indexOf(qLower);
  if (idx === -1) return content.slice(0, 120).replace(/\n/g, " ").trim();
  const start = Math.max(0, idx - 60);
  const end = Math.min(content.length, idx + query.length + 80);
  let snippet = content.slice(start, end).replace(/\n/g, " ").trim();
  if (start > 0) snippet = "…" + snippet;
  if (end < content.length) snippet = snippet + "…";
  return snippet;
}

export function handleSearch(cfg: ServerConfig) {
  return (req: Request, res: Response) => {
    const q = ((req.query.q as string) ?? "").trim();
    if (q.length < 1) {
      res.json({ hits: [] });
      return;
    }

    const qLower = q.toLowerCase();
    const files = walkMd(cfg.wikiRoot, cfg.wikiRoot);
    const hits: SearchHit[] = [];

    for (const file of files) {
      try {
        const content = fs.readFileSync(file, "utf-8");
        if (!content.toLowerCase().includes(qLower)) continue;

        const rel = path.relative(cfg.wikiRoot, file).split(path.sep).join("/");
        hits.push({
          path: rel,
          title: extractTitle(content, file),
          snippet: buildSnippet(content, q),
        });

        if (hits.length >= 15) break;
      } catch {
        continue;
      }
    }

    res.json({ hits });
  };
}
