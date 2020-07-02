class Vertex {
  constructor(val) {
    this.val = val;
  }

  toString() {
    return this.val.toString();
  }
}

const v1 = new Vertex(1);
const v2 = new Vertex(2);

const ht = {};
ht[v1] = 1;
ht[v2] = 2;

console.log(ht);
console.log(ht[v1]);
console.log(ht[v2]);
