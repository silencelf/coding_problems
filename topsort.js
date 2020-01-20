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
    for(const v of u.neighbors) {
      if (indegrees[v.val]) {
        indegrees[v.val]++;
      } else {
        indegrees[v.val] = 1;
      }
    }
  }

  console.log(indegrees);
  return;
  const sorted = [];
  const leaves = vertexes.filter(v => v.neighbors.length === 0);
  while (leaves.length > 0) {
    for (const l of leaves) {
      sorted.push(l);
      for (const parent of reverse[l]) {
        parent
      }
    }
  }
  // compute the out-degree of vertexes
}

const g = new Vertex('G', []);
const f = new Vertex('F', [g]);
const d = new Vertex('D', [f]);
const e = new Vertex('E', [f]);
const c = new Vertex('C', [e]);
const a = new Vertex('A', [c]);
const b = new Vertex('B', [c, d]);
const graph = [a, b, c, d, e, f, g];
// const sorted = topSort(graph);
// console.log(sorted.reverse());

bfsTopSort(graph);
