// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography;

Console.WriteLine("Ingrese un número");
int num = int.Parse(Console.ReadLine()!);

if (num > 0)
{
    Console.WriteLine("El número ingresado es positivo");
}
else if (num < 0)
{
    Console.WriteLine("El número ingresado es negativo");
}
else if (num == 0)
{
    Console.WriteLine("El nuúmero ingresado es 0");
}