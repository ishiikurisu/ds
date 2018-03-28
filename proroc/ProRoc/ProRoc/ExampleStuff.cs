using ExcelDna.Integration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProRoc
{
    public static class ExampleStuff
    {

        [ExcelFunction(Description = "My first Excel function")]
        public static string SayHi(string who)
        {
            return "Hi " + who;
        }
    }
}
