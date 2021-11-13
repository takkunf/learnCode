/*
import "dart:io";

void main() {
 
  stdout.writeln("Insert your name");
  var name = stdin.readLineSync();

  stdout.writeln("Insert your age");
  var age = stdin.readLineSync();

  stdout.writeln("Insert your favorite food");
  var food = stdin.readLineSync();

  print(
      "Hello my name is $name, I am $age years old and my favorite food is $food");
}

//Lenguajes fuertemente tipados: 
  El tipo de una variable se conoce en tiempo de compilacio:
  jave, c++, swift

//Lenguaje de tipo dinamico:
  El tipo de una variable se conoce en tiempo de ejecucion:
  python, ruby, javascript

//Tipo de datos en Dart: int, double, string, bool, dynamic

void main() {
  int edad1 = 10;
  var edad2 = 15;
  print("Las edades ingresadas son: $edad1 y $edad2");

  double sueldo1 = 500.25;
  var sueldo2 = 620.99;
  print("Los sueldos ingresados son: $sueldo1 y $sueldo2");

  String nombre1 = "Ricky";
  var nombre2 = "Takumi";
  print("El nombre ingresado es: $nombre1 $nombre2");

  bool valor1 = true;
  var valor2 = true;
  print("los valores ingresados son $valor1 y $valor2");

  dynamic dyvalor1 = 'Alexx';
  print("El valor de dyvalor es $dyvalor1");
  dyvalor1 = 15;
  print("El valor de dyvalor es $dyvalor1");
  dyvalor1 = null;
  print("El valor de dyvalor es $dyvalor1");
}

void main() {
  var s1 = 'Una cadena se puede crear con comillas simples';
  var s2 = "Una cadena se puede crear con comillas dobles";
  var s3 = 'It\'s es una oracion'; //It's
  var s4 = "It's es una oracion";
  var s5 = r'Esto es una cadena que \n puede ser muy extensa';
  var s6 = '''
  Usted esta creando un texto
  de multiples lineas
  '''; // se puede usar comillas simples (') o dobles ("")

  //Conversion de String -> Int
  var uno = int.parse('1');
  assert(uno == 1);

  //Conversion de String -> double
  var pi = double.parse('3.1415926535');
  assert(pi == 3.1415926535);

  //Conversion de Int -> String
  var unoAString = 1.toString();
  assert(unoAString == '1');

  //Conversion de double -> String
  var py = 3.1415926535.toStringAsFixed(10);
  assert(py == '3.1415926535');
}

void main() {
  //Operadores matematicos
  int num = 30;
  num = num + 22;
  print(num);

  num = num % 2;
  print(num);

  //Operadores logicos ==, !=, <=, >=
  if (num == 0) {
    print('cero');
  } else {
    print('No es cero');
  }
  //Operadores Unarios
  num = 5;
  //++num;
  print(++num);
  //num++;
  print(num++);
  print(num);

  //Logico AND  (&&), logico OR(||)
  num = 202;
  if ((num > 200) && (num < 205)) {
    print('Verdadero');
  } else {
    print("False");
  }

  //Operador bitwise
  var a = 2;
  var b = 3;

  //4 2 1
  //0 1 0
  //0 1 1
  //-----
  //0 1 0

  var resultado = (a & b);
  print(resultado);
  resultado = (a | b);
  print(resultado);
}

void main() {
  //Sentencias condicionales
  //Sentecia if
  int numero = 99;

  if (numero % 2 == 0) {
    print("Multiplo de 2");
  } else {
    if (numero % 3 == 0) {
      print("Multiplo de 3");
    } else {
      print("No es multiplo de ninguno");
    }
  }
}

void main() {
  //Sentencia switch
  int numero = 6;

  switch (numero) {
    case 1:
      print("Enero");
      break;
    case 2:
      print("Febrero");
      break;
    case 3:
      print("Marzo");
      break;
    case 4:
      print("Abril");
      break;
    case 5:
      print("Mayo");
      break;
    case 6:
      print("Junio");
      break;
  }
}


void main() {
  //Sentencia repetitivas - Loops

  var numeros = [4, 8, 16];

  for (int i = 0; i <= 2; i++) {
    print(numeros[i]);
  }

  for (var n in numeros) {
    print(n);
  }
  numeros.forEach((n) => print(n));
  
  var num = 0;

  while (num > 0) {
    print(num);
    num--;
  }
  num = 6;
  do {
    print(num);
    num++;
  } while (num <= 5);
  
}

void main() {
  // Colecciones en Dart
  List<String> nombres = ['Jack', 'Pablo'];

  var nombres2 = [...nombres];
  nombres[1] = 'Ana';

  for (var n in nombres2) {
    print(n);
  }
  print(nombres.length);
  print(nombres2.length);
  var frutas = {'fruta1': 'Manzana', 'fruta2': 'Pera', 3: 'Mango'};

  var persona = {'nombre': 'Pablo', 'edad': 35, 'novia': 'Ana'};

  print(frutas[3]);
  print(persona['edad']);
}

void main() {
  //Funciones en Dart, Arraw function =>
  mostrarSalida('Hola Mundo');
  mostrarSalida(raizCuadrada(3.5));

  var list = ['Manzanas', 'Bananas', "Naranjas"];
  list.forEach((item) => print(item));
}

//dynamic printSalida(var item) => print(item);

void mostrarSalida(var msj) => print(msj);

dynamic raizCuadrada(var num) => num * num;

//Clases y objetos

class Persona {
  String nombre = "";
  int edad = 0;

  Persona(String this.nombre, [int this.edad = 18]);

  Persona.guest() {
    this.nombre = "Pedro";
    this.edad = 20;
  }
  Persona.prueba(String name) {
    this.nombre = name;
    this.edad = 24;
  }

  void mostrarDatos() {
    print(nombre);
    print(edad);
  }
}

class X {
  final nombre;
  static const int edad = 10;

  X(this.nombre);
}

void main() {
  var x = X("Jack");
  print(x.nombre);

  print(X.edad);

  Persona persona1 = Persona("Takumi", 25);
  persona1.mostrarDatos();

  Persona persona2 = Persona("Ana");
  persona2.mostrarDatos();

  Persona persona3 = Persona.guest();
  persona3.mostrarDatos();

  Persona persona4 = Persona.prueba("Alex");
  persona4.mostrarDatos();
}
*/
