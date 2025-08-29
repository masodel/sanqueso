// See https://aka.ms/new-console-template for more information
Console.WriteLine("Ingrese un número del 1 al 7");
int num = int.Parse(Console.ReadLine()!);
string dia;

if (num > 0 && num < 7)
{
    switch (num)
    {
        case 1:
            dia = "Lunes";
            break;

        case 2:
            dia = "Martes";
            break;

        case 3:
            dia = "Miércoles";
            break;

        case 4:
            dia = "Jueves";
            break;

        case 5:
            dia = "Viernes";
            break;

        case 6:
            dia = "Sábado";
            break;

        case 7:
            dia = "Domingo";
            break;
    }
    Console.WriteLine($"El día escogido fue {dia}");
}
else
{
    Console.WriteLine("Número inválido, intente de nuevo");
}