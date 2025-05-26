from manim import *
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


def lorenz_system(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0=state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T



class LorenzAttractor(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        # Set up axes
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(-0, 50, 5),
        )
        axes.center()
        self.add(axes)
        
        # Display Lorentz solutions
        state0 = [10, 10, 10]
        points = ode_solution_points(lorenz_system, state0, 10)

        curve = VMobject().set_points_as_corners(axes.c2p(*points))
        self.play(ShowCreation(curve, run_time=10))
        
        
