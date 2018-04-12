using ExcelDna.Integration;
using System;
using System.Collections.Generic;
using System.IO;
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

        /// <summary>
        /// Uses the PROMETHEE model to assess the best action.
        /// </summary>
        /// <param name="weights">The list of weights for each criteria. Should have the same
        /// length as the criteria array.</param>
        /// <param name="table">The rankings for each criteria, thus comparing each action.
        /// Should have the same number of lines as actions and the same number of
        /// columns as criteria.</param>
        /// <returns>The flow for each action in given order.</returns>
        [ExcelFunction(Description = "Uses the PROMETHEE model to assess the best action.")]
        public static double[] Promethee(double[] weights, double[,] table)
        {
            int n = table.GetLength(0);
            var flow = new double[n];

            // Fact checking
            if (table.GetLength(1) != weights.GetLength(0))
            {
                return flow;
            }

            // Calculating preferences
            var prefs = new double[n, n];
            for (int a = 0; a < table.GetLength(0); a++)
            {
                for (int b = 0; b < table.GetLength(0); b++)
                {
                    double p = 0;
                    for (int j = 0; j < table.GetLength(1); ++j)
                    {
                        p += (table[a, j] - table[b, j]) * weights[j];
                    }
                    prefs[a, b] = p;
                }
            }

            // Calculating flow
            for (int a = 0; a < n; a++)
            {
                double phi_p = 0;
                double phi_m = 0;

                for (int b = 0; b < n; b++)
                {
                    phi_p += prefs[a, b];
                    phi_m += prefs[b, a];
                }

                flow[a] = (phi_p - phi_m) / n;
            }

            return flow;
        }

        /// <summary>
        /// Turns a matrix into a string for debugging purposes.
        /// </summary>
        /// <param name="matrix">The input matrix</param>
        /// <returns></returns>
        public static string Matrix2String(double[,] matrix)
        {
            string outlet = "";

            for (int i = 0; i < matrix.GetLength(0); ++i)
            {
                string line = matrix[i, 0].ToString();
                for (int j = 1; j < matrix.GetLength(1); ++j)
                {
                    line += $" {matrix[i, j]}";
                }
                outlet += line + "\n";
            }

            return outlet;
        }
    }
}
