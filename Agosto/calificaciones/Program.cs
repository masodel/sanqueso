Console.Write("Ingresa tu calificación: ");
int num = int.Parse(Console.ReadLine()!);

if (num >= 70 && num <= 100)
{
    Console.WriteLine("Clase aprobada");
}

else if (num < 70 && num >= 50)
{
    Console.WriteLine("Estás en recuperación");
}

else if (num < 50 && num >= 0)
{
    Console.WriteLine("Clase reprobada");
}

else
{
    Console.WriteLine("Clasificación inválida");
}