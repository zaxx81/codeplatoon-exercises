let bp = require("./balanceParens");

console.log(bp.balanceParens("a)b))c(d)e(fgh))(i)j)(((k(") === "abc(d)e(fgh)(i)jk")
console.log(bp.balanceParens("abc((d)e(fgh)(i)j(k") === "abc(d)e(fgh)(i)jk")
console.log(bp.balanceParens("()") === "()")
console.log(bp.balanceParens("a(b)c)") === "a(b)c")
console.log(bp.balanceParens("(a)(bdd)c)") === "(a)(bdd)c")
console.log(bp.balanceParens("a(dbvb)c)") === "a(dbvb)c")
console.log(bp.balanceParens("a(b)(c)())") === "a(b)(c)()")
console.log(bp.balanceParens(")(") === "")
console.log(bp.balanceParens("(((((") === "")
console.log(bp.balanceParens(")(())(") === "(())")
console.log(bp.balanceParens("(()()(") === "()()")
console.log(bp.balanceParens(")())(()()(") === "()()()")
console.log(bp.balanceParens("abc(d)(ef(g(h))ij)k)lm()o)p") === "abc(d)(ef(g(h))ij)klm()op")
console.log(bp.balanceParens(")(())(") === "(())")