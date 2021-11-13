import 'dart:math';

main() {
  var ages = [33, 15, 27, 40, 22];

  print("""
  La edad mayor es: ${ages.reduce(max)}
  La edad menor es: ${ages.reduce(min)}
  La edad promedio es: ${ages.reduce((cur, next) => cur + next) / ages.length}
  """);
}
