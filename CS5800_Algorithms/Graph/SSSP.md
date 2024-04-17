# Single Source Shortest Path (SSSP)

## Recap: SSSP

- G = (V, E) where:
  - (u, v) ∈ E
  - w[u, v] (Weight of edge from u to v)
- Source Vertex `s`
- Shortest path from `s` to `∀ u ∈ U`
  - `dist[u]`
  - `π[u]`

Is G a DAG (Directed Acyclic Graph)?

- Are edges directed (Y/N)?
- Are weights >= 0 (Y/N)?

|                  | Directed            | Not Directed                       |
| ---------------- | ------------------- | ---------------------------------- |
| **Weights >= 0** | SSSP on DAG: O(m+n) | Dijkstra's: O(n^2) or O((m+n)logn) |
| **Weights < 0**  | Bellman-Ford: O(nm) | Bellman-Ford: O(nm)                |

```
relax(u, v)
if dist[u] + w[u, v] < dist[v]
  dist[v] = dist[u] + w[u, v]
  π[v] = u
```

---
