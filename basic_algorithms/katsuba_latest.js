const split = number => {
  const n = number.toString().length;
  if (!isFinite(number) || n === 1) {
    throw Error(`Cannot split number = ${number}`);
  }

  const n2 = Math.floor(n / 2);
  const divider = 10 ** n2;

  const num1 = Math.floor(number / divider);
  const num2 = number % divider;

  return [num1, num2];
};

const karatsuba = (integer1, integer2) => {
  if (integer1 < 10 || integer2 < 10) {
    return integer1 * integer2;
  }

  const n = Math.max(integer1.toString().length, integer2.toString().length);
  const n2 = Math.floor(n / 2);

  const [a, b] = split(integer1);
  const [c, d] = split(integer2);

  const ac = karatsuba(a, c);
  const bd = karatsuba(b, d);
  const abcd = karatsuba(a + b, c + d);
  const magic = abcd - ac - bd;

  return ac * 10 ** (2 * n2) + magic * 10 ** n2 + bd;
};

function toFixed(x) {
  if (Math.abs(x) < 1.0) {
    var e = parseInt(x.toString().split("e-")[1]);
    if (e) {
      x *= Math.pow(10, e - 1);
      x = "0." + new Array(e).join("0") + x.toString().substring(2);
    }
  } else {
    var e = parseInt(x.toString().split("+")[1]);
    if (e > 20) {
      e -= 20;
      x /= Math.pow(10, e);
      x += new Array(e + 1).join("0");
    }
  }
  return x;
}

console.log(karatsuba(12, 12).toString(10));
console.log(karatsuba(0, 0).toString(10));
console.log(karatsuba(1234, 5678).toString(10));
let result = karatsuba(
  3141592653589793238462643383279502884197169399375105820974944592,
  2718281828459045235360287471352662497757247093699959574966967627
);
let s = result.toString(10);
let sBuild = "";
// s.forEach(element => {
//   sBuild += element;
// });
console.log(sBuild);
console.log(result);
console.log(Math.floor(result));
console.log(parseFloat(result));
console.log(toFixed(result));
