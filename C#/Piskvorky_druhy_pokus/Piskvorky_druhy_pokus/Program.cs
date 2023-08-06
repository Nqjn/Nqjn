using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.Design;
using System.Globalization;
using System.Linq;
using System.Media;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace Piskvorky_druhy_pokus
{
    internal class Program
    {
        static int gcnt = 0;
        static string[] field = { "1", "2", "3", "4", "5", "6", "7", "8", "9", };
        static string[] arr = { };

        static bool gameOver = false;


        static void Main(string[] args)
        {
            bool game = true;
            
            

            /* Hlavni herni cyklu*/
            while (game == true)
            {
                DrawPlayfield();
                Play("X");
                Console.Clear();
                
                if (gameOver == true)
                {
                    Console.WriteLine("Hráč 1 vyhrál");
                    break;
                }

                /* Kontrola remízy*/
                gcnt++;
                if (gcnt == 5)
                {
                    Console.WriteLine("Remíza");
                    break;
                }
                
                DrawPlayfield();
                Play("O");
                Console.Clear();
                
                
                if (gameOver == true)
                {
                    Console.WriteLine("Hráč 2 vyhrál");
                    break;
                }
            }
        }

        static void Play(string player)
        {
            bool occupied = true;


            while (occupied == true)
            {

                Console.WriteLine("Na tahu je " + player);

                int move1 = Convert.ToInt32(Console.ReadLine());
                string l = Convert.ToString(move1);

                /*Kontrola jestli je pole obsazene */
                string searchElemnt = l;
                bool exists = Array.Exists(arr, element => element == searchElemnt);
                if (exists)
                {
                    Console.WriteLine("Pole už je obsazené");
                }

                else
                {
                    field[move1 - 1] = player;
                    arr = arr.Append(l).ToArray();
                    occupied = false;
                }

                /*Kontrola obsazenosti */
                if (Check(player))
                {
                    gameOver = true;
                }               
            }
        }

        static void DrawPlayfield()
        {
            Console.Write("|");
            for (int i = 0; i < field.Length; i++)
            {
                Console.Write(field[i] + "|");
                if ((i + 1) % 3 == 0)
                {
                    Console.WriteLine("");
                    /*  dělá řádky */
                    if (i == 8)
                    {
                        Console.WriteLine("");
                    }
                    else
                    {
                        Console.WriteLine("-------");
                    }
                    
                    /* Dává | na další řádek, pokud není poslední */
                    if (i == 8)
                    {
                        Console.WriteLine("");
                    }
                    else
                    {
                        Console.Write("|");
                    }
                      
                }

            }
        }
        static bool Check(string player)
        {
            int cnt = 0;
            int cntd1 = 0;
            int cntd2 = 0;

            for (int c = 0; c < 3; c++)
            {
                /* Kontrola sloupce a řádku*/
                cnt = 0;

                for (int r = 0; r < 3; r++)
                {
                    if (field[3 * c + r] == player) cnt++;

                }

                if (cnt == 3)
                {
                    return true;
                }

                cnt = 0;
                for (int cl = 0; cl < 7; cl = cl + 3)
                {
                    if (field[cl + c] == player) cnt++;
                }

                if (cnt == 3)
                {
                    return true;
                }
            }

                            
            /* Kontrola uhlopříček */

             for (int d1 = 0; d1 < 9; d1 = d1 + 4)
            {
                if (field[d1] == player) cntd1++;

            }
            if (cntd1 == 3)
            {


                return true;

            }

            for (int d2 = 2; d2 < 7; d2 = d2 + 2)
            {
                if (field[d2] == player) cntd2++;

            }

            if (cntd2 == 3)
            {
                return true;
            }
          
        return false;

        }
    }

}
