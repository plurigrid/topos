# Julia Exploration

using Pkg

# Function to install and import packages
function setup_packages(packages)
    for package in packages
        try
            Pkg.add(package)
        catch e
            println("Error installing $package: $e")
        end
    end
end

# List of packages we want to explore
packages = ["DataFrames", "Plots", "Flux", "DifferentialEquations"]

println("Setting up Julia packages...")
setup_packages(packages)

# Import the packages
using DataFrames
using Plots
using Flux
using DifferentialEquations

# Example: Create a DataFrame
df = DataFrame(A = 1:4, B = ["M", "F", "F", "M"])
println("Example DataFrame:")
println(df)

# Example: Create a simple plot
x = 1:10
y = x.^2
plot(x, y, title="Square Function", label="y = x^2", xlabel="x", ylabel="y")
savefig("square_function.png")
println("Created a plot: square_function.png")

# Example: Simple neural network with Flux
model = Chain(
  Dense(10, 5, relu),
  Dense(5, 2),
  softmax)

println("Neural Network Structure:")
println(model)

# Example: Solve a differential equation
function lorenz!(du, u, p, t)
    σ, ρ, β = p
    du[1] = σ*(u[2]-u[1])
    du[2] = u[1]*(ρ-u[3]) - u[2]
    du[3] = u[1]*u[2] - β*u[3]
end

u0 = [1.0, 0.0, 0.0]
tspan = (0.0, 100.0)
p = [10.0, 28.0, 8/3]
prob = ODEProblem(lorenz!, u0, tspan, p)
sol = solve(prob)

plot(sol, vars=(1,2,3), title="Lorenz Attractor")
savefig("lorenz_attractor.png")
println("Solved Lorenz equations and created plot: lorenz_attractor.png")

println("Julia exploration complete!")
