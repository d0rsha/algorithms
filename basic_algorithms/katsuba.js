let karatsuba = function(x, y) {
  let n = Math.max(x.toString(10).length, y.toString(10).length);
  let m = Math.floor(n / 2);

  // base case
  if (n == 1) return x * y;

  // Recursive case
  let a = Math.floor(x / Number(10 ** m));
  let b = x % Number(10 ** m);

  let c = Math.floor(y / Number(10 ** m));
  let d = y % Number(10 ** m);

  let = p = a + b;
  let = q = c + d;

  ac = karatsuba(a, c);
  bd = karatsuba(b, d);
  pq = karatsuba(p, q);

  adbc = pq - ac - bd;

  return Number(
    Number(10 ** n) * ac + Number(10 ** (n / 2)) * adbc + Number(bd)
  );
};

console.log(karatsuba(12, 12).toString(10));
console.log(karatsuba(0, 0).toString(10));
console.log(karatsuba(1234, 5678).toString(10));
console.log(
  karatsuba(
    3141592653589793238462643383279502884197169399375105820974944592,
    2718281828459045235360287471352662497757247093699959574966967627
  ).toString(10)
);
