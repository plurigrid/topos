import modal

image = modal.Image.debian_slim().apt_install(
    "wget", "ca-certificates"
).run_commands(
    "wget -nv https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.3-linux-x86_64.tar.gz",
    "tar -xf julia-1.9.3-linux-x86_64.tar.gz",
    "cp -r julia-1.9.3 /opt/",
    "ln -s /opt/julia-1.9.3/bin/julia /usr/local/bin/julia",
).pip_install("julia==0.6.1").run_commands(
    'python -c "import julia; julia.install()"'
)

app = modal.App("example-pyjulia", image=image)

@app.function()
def julia_subprocess():
    """Run the Julia interpreter as a subprocess."""
    import subprocess

    print("-> Calling Julia as a subprocess...")
    subprocess.run('julia -e "println(2 + 3)"', shell=True)

@app.function()
def julia_matrix_determinant():
    """Compute the determinant of a random matrix with PyJulia."""
    from julia.Base import rand
    from julia.LinearAlgebra import det

    print("-> Calling Julia using PyJulia...")
    print(det(rand(5, 5)))
    print(det(rand(10, 10)))

def run_modal_julia_app():
    julia_subprocess.remote()
    julia_matrix_determinant.remote()
