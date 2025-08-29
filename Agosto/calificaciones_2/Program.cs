Console.Write("Ingresa tu calificación: ");
int num = int.Parse(Console.ReadLine()!);
switch (num)
{
    case >=70 and <=100:
        Console.WriteLine("Asignatura aprobada");
        break;
    case >=50 and <70:
        Console.WriteLine("Estás en recuperación");
        break;
    case >=0 and <50:
        Console.WriteLine("Asignatura reprobada");
        break;
    default:
        Console.WriteLine("Calificación inválida, intento nuevamente");
        break;
}