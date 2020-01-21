class Vertex {
  val = NaN;
  neighbors = [];

  constructor(val, neighbors) {
    this.val = val;
    this.neighbors = neighbors;
  }
}

function topSort(vertexes) {
  const visited = new Set();
  const stack = [];

  for(const vertex of vertexes) {
    if(visited.has(vertex))
      continue;
    dfs(vertex, visited, stack);
  }

  return stack;
}

function dfs(vertex, visited, stack) {
  visited.add(vertex);

  for (const n of vertex.neighbors) {
    if(visited.has(vertex))
      continue;
    dfs(n, visited, stack);
  }

  stack.push(vertex.val);
  console.log(stack);
}

function bfsTopSort(vertexes) {
  // create a in-degree tables
  const indegrees = {};
  for(const u of vertexes) {
    indegrees[u.val] = {
      in: 0,
      ref: u
    };
  }
  for(const u of vertexes) {
    for(const v of u.neighbors) {
      indegrees[v.val].in++;
    }
  }
  let roots = [];
  for(const k in indegrees) {
    const item = indegrees[k];
    if (item.in == 0) {
      roots.push(item.ref);
    }
  }
  const sorted = [];
  while (roots.length > 0) {
    const newRoots = [];
    console.log('new roots:')
    console.log(roots);
    for (const leaf of roots) {
      sorted.push(leaf.val);
      for (const child of leaf.neighbors) {
        indegrees[child.val].in--;
        if (indegrees[child.val].in == 0) {
          newRoots.push(child);
        }
      }
    }
    roots = newRoots;
  }

  return sorted.reverse();
}

const g = new Vertex('G', []);
const f = new Vertex('F', [g]);
const d = new Vertex('D', [f]);
const e = new Vertex('E', [f]);
const c = new Vertex('C', [e]);
const a = new Vertex('A', [c]);
const b = new Vertex('B', [c, d]);
const graph = [a, b, c, d, e, f, g];
// dfs
// const sorted = topSort(graph);
// console.log(sorted.reverse());

// bfs
const sorted = bfsTopSort(graph);
console.log(sorted);
