// See https://aka.ms/new-console-template for more information
Console.WriteLine("Ingresa el año");
int anio = int.Parse(Console.ReadLine()!);

if (num % 4 == 0 && num % 100 != 0 || num % 400 == 0)
{
    Console.WriteLine("El año es bisiesto");
}

else
{
    Console.WriteLine("El año no es bisiesto");
}