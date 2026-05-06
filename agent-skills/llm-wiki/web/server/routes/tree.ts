import fs from "node:fs";
import path from "node:path";
import type { Request, Response } from "express";
import type { ServerConfig } from "../config.js";

export interface TreeNode {
  name: string;
  path: string; // relative to wikiRoot
  kind: "file" | "dir";
  children?: TreeNode[];
}

/**
 * Build a navigation tree from the wiki/ directory.
 * The tree is recursive, sorted alphabetically, and only includes .md files.
 */
export function buildTree(wikiRoot: string): TreeNode {
  const wikiDir = path.join(wikiRoot, "wiki");
  if (!fs.existsSync(wikiDir)) {
    return { name: "wiki", path: "wiki", kind: "dir", children: [] };
  }
  return walk(wikiRoot, wikiDir, "wiki");
}

function readTitle(filePath: string, fallback: string): string {
  try {
    const content = fs.readFileSync(filePath, "utf-8");
    const m = content.match(/^#\s+(.+)$/m);
    if (m) return m[1]!.trim();
  } catch {}
  return fallback;
}

function isDir(full: string): boolean {
  try {
    return fs.statSync(full).isDirectory();
  } catch {
    return false;
  }
}

function walk(wikiRoot: string, dir: string, rel: string): TreeNode {
  const entries = fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((e) => !e.name.startsWith("."))
    .sort((a, b) => {
      const aIsIndex = a.name === "index.md";
      const bIsIndex = b.name === "index.md";
      if (aIsIndex !== bIsIndex) return aIsIndex ? -1 : 1;
      const aDir = isDir(path.join(dir, a.name));
      const bDir = isDir(path.join(dir, b.name));
      if (aDir !== bDir) return aDir ? -1 : 1;
      return b.name.localeCompare(a.name);
    });

  const children: TreeNode[] = [];
  for (const e of entries) {
    const full = path.join(dir, e.name);
    const nodeRel = path.posix.join(rel, e.name);
    if (isDir(full)) {
      children.push(walk(wikiRoot, full, nodeRel));
    } else if (e.name.endsWith(".md")) {
      const fallback = e.name.replace(/\.md$/, "");
      children.push({ name: readTitle(full, fallback), path: nodeRel, kind: "file" });
    }
  }

  return { name: path.basename(dir), path: rel, kind: "dir", children };
}

export function handleTree(cfg: ServerConfig) {
  return (_req: Request, res: Response) => {
    res.json(buildTree(cfg.wikiRoot));
  };
}
