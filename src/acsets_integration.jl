using Pkg
Pkg.add("ACSets")
using ACSets

function create_simple_acset()
    @acset_type SimpleGraph(V::Int, E::Int, src::V, tgt::V)
    g = SimpleGraph()
    add_parts!(g, :V, 3)
    add_parts!(g, :E, 2, src=[1,2], tgt=[2,3])
    return g
end

function analyze_acset(acset)
    println("ACSets Analysis:")
    println("Number of vertices: ", nparts(acset, :V))
    println("Number of edges: ", nparts(acset, :E))
    println("Edges: ", collect(zip(acset[:src], acset[:tgt])))
end

function main()
    g = create_simple_acset()
    analyze_acset(g)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
