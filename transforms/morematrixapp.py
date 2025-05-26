from manim import *


class MoreApplyMatrixExamples(Scene):
    def construct(self):


        def compute_matrix_inverse(matrix):
            """
            Compute the inverse of a matrix using NumPy

            Parameters:
            matrix: array_like
                Input matrix to invert (must be square and non-singular)

            Returns:
            numpy.ndarray
                Inverse of the input matrix

            Raises:
            LinAlgError: If matrix is singular or not square
            """
            try:
                # Convert input to numpy array if it isn't already
                matrix = np.array(matrix, dtype=float)

                # Check if matrix is square
                if matrix.shape[0] != matrix.shape[1]:
                    raise ValueError("Matrix must be square")

                # Compute the inverse
                inverse = np.linalg.inv(matrix)

                return inverse

            except np.linal.LinAlgError:
                raise np.linalg.LinAlgError(
                    "Matrix is singular and cannot be inverted"
                )
            
        
        matrix = [[1, 2], [0, 4]]
        t_matrix = [[1, 0], [2, 4]]
        inv_matrix = compute_matrix_inverse(matrix) # [[1, -1/2], [0, 1/4]]
        t_inv_matrix = compute_matrix_inverse(t_matrix) # [[1, 0], [-1/2, 1/4]]
        
        texwar = Tex(r"\TeX vs \LaTeX")
        num_plan = NumberPlane()
        matrices = [matrix, t_matrix]
        inv_matrices = [inv_matrix, t_inv_matrix]
        
        for i in range(len(matrices)):
            m = Matrix(matrices[i], left_bracket="[", right_bracket="]")
            self.play(
                Write(m.to_edge(UL)),
                ApplyMatrix(matrices[i], texwar),
                ApplyMatrix(matrices[i], num_plan)
            )
            self.wait(2)
            
            im = Matrix(inv_matrices[i], left_bracket="[", right_bracket="]")
            self.play(
                Write(im.to_edge(DR)),
                ApplyMatrix(inv_matrices[i], texwar),
                ApplyMatrix(inv_matrices[i], num_plan)
            )
            self.wait(2)
            

            self.play(
                FadeOut(m, im)
            )
            
        
