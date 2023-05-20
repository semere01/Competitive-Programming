class Union {
  late List<int> data;

  Union(int size) {
    this.data = List.generate(size, (index) => index);
  }

  int rep(int x) {
    List<int> stack = [x];
    while (stack.isNotEmpty) {
      int current = stack.last;
      if (current == data[current]) {
        return current;
      } else {
        stack.add(this.data[current]);
      }
    }
    throw Exception();
  }

  void join(int x, int y) {
    int x_rep = rep(x);
    int y_rep = rep(y);

    data[x_rep] = data[y_rep];
  }
}

class Solution {
  int manDistance(List<int> p1, List<int> p2) {
    int x = (p1[0] - p2[0]).abs();
    int y = (p1[1] - p2[1]).abs();
    return x + y;
  }

  int minCostConnectPoints(List<List<int>> points) {
    List<List<int>> distances = [];
    Union union = Union(points.length);
    for (var x = 0; x < points.length; x++) {
      for (var y = 0; y < points.length; y++) {
        distances.add([x, y, manDistance(points[x], points[y])]);
      }
    }
    distances.sort((a,b) =>a[2].compareTo(b[2]));
    int minCost = 0;
    int counter = 0;

    for (var distance in distances) {
      if (union.rep(distance[0]) != union.rep(distance[1])) {
        union.join(distance[0], distance[1]);
        minCost += distance[2];
        counter += 1;
        if (counter == points.length - 1) {
          break;
        }
      }
    }
    return minCost;
  }
}
