using ExcelDna.Integration;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProRoc
{
    public static class Model
    {
        /// <summary>
        /// Turns a list of numbers into ROC weights. WARNING! Doesn't check the input 
        /// consistency yet.
        /// </summary>
        /// <param name="ranking">The original weights ranking. Must be a list of integers 
        /// containing all integers from 1 to n, where n is the length of the list.</param>
        /// <returns>The converted ROC weights</returns>
        [ExcelFunction(Description = "Turns a list of numbers into ROC weights.")]
        public static double[] Roc(double[] ranking)
        {
            int n = ranking.Length;
            double[] w = new double[n];

            // IDEA Check input consistency, that is, if it contains only numbers from 1 to n.
            for (int i = 0; i < n; ++i)
            {
                double j = ranking[i];
                double wj = 0;
                for (double k = j; k <= n; ++k)
                {
                    wj += 1 / k;
                }
                w[i] = wj/n;
            }

            return w;
        }
    }
}
