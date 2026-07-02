

var decimalNumber = 3.14; 
// Print
Console.WriteLine($"Hey The value of pi is {decimalNumber}");

// Name  

Console.WriteLine("What is your name?");
string name = Console.ReadLine();
Console.WriteLine($"Nice to meet you, {name}!");

// Age confirmation

Console.WriteLine("How old are you?");
string ageInput = Console.ReadLine();
int age = Convert.ToInt16(ageInput);
Console.WriteLine($"You are {age} years old.? y/n");
var input = Console.ReadLine();
if (input == "y")
{
    Console.WriteLine();
    Console.WriteLine("Great!");
    Console.WriteLine();
}
else
{
    Console.WriteLine("So what is your age?");
    string newAgeInput = Console.ReadLine();
    int newAge = Convert.ToInt16(newAgeInput);
    Console.WriteLine($"You are {newAge} years old.");
}


// Passowrd confirmation

Console.WriteLine("What is your password?");
string password = Console.ReadLine();

Console.WriteLine("Please enter your password again to confirm:");
string confirmPassword = Console.ReadLine();

if (password == confirmPassword)
{
    Console.WriteLine("Password confirmed.");
}
else
{
    Console.WriteLine("Passwords do not match. Please try again.");
}

Console.WriteLine("Press any key to exit.");
    if (Console.ReadKey().Key == ConsoleKey.Enter)
    {
        Environment.Exit(0);
    }
    
