/*
 * Return true if there is a path from cur to target.
 */

# 这个是dfs的递归形式的模板，也就是用系统栈。
# 这个模板用来找路径中有没有target这个数。 其他任务灵活变通即可。
# 需要注意的是，python中list，dict都是引用传递，因此两者作为参数时，可以改变外部值。
# 也就实现了代码中的 visited 作为参数并在函数内改变的功能。

boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visted;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}