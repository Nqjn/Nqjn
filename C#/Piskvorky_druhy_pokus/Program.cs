using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Piskvorky_druhy_pokus
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] arr = { };
            string[] field = { "1", "2", "3", "4", "5", "6", "7", "8", "9", };
            bool controler1 = false;
            bool controler2 = false;

            for (int p = 0; p < field.Length; p++)
            {
                Console.Write(field[p] + ",");
                if ((p + 1) % 3 == 0)
                {
                    Console.WriteLine();

                }
            }

            /* Hlavni herni cyklus, dodelat statut hry*/
            for (int j = 1; j > 0; j++)
            {
                /* Rozhoduje o tahu hrace  */

                /* hrac 1 */

                
                if (j % 2 == 0)
                {
                    
                    Console.WriteLine("Zahraj svuj tah");
                    int move1 = Convert.ToInt32(Console.ReadLine());
                    string l = Convert.ToString(move1);
                    string searchElemnt = l;
                    bool exists = Array.Exists(arr, element => element == searchElemnt);
                    if (exists)
                    {
                        Console.WriteLine("Pole uz je obsazene");
                    }
                    else
                    {
                        field[move1 - 1] = "X";
                        arr = arr.Append(l).ToArray();

                    }
                /* hrac 2*/
                }
                else
                {
                    Console.WriteLine("Zahraj svuj tah");
                    int move1 = Convert.ToInt32(Console.ReadLine());
                    string l = Convert.ToString(move1);
                    string searchElemnt = l;
                    bool exists = Array.Exists(arr, element => element == searchElemnt);
                   
                    if (exists)
                    {
                        Console.WriteLine("Pole uz je obsazene");
                    }
                    else
                    {
                        field[move1 - 1] = "O";
                        arr = arr.Append(l).ToArray();

                    }
                }
                /* Generovani herniho pole*/
                for (int i = 0; i < field.Length; i++)
                {
                    Console.Write(field[i] + ",");
                    if ((i + 1) % 3 == 0)
                    {
                        Console.WriteLine();

                    }
                                                                                                                    
                }
            }
        }
    }
}
