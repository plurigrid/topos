from typing import Dict, Any, Callable

class Actegory:
    def __init__(self, name: str):
        self.name = name
        self.objects: Dict[str, Any] = {}
        self.morphisms: Dict[str, Callable] = {}

    def add_object(self, obj_name: str, obj: Any):
        self.objects[obj_name] = obj

    def add_morphism(self, morph_name: str, morph: Callable):
        self.morphisms[morph_name] = morph

    def compose(self, f_name: str, g_name: str) -> Callable:
        f = self.morphisms[f_name]
        g = self.morphisms[g_name]
        return lambda x: f(g(x))

def actegory_functor(source: Actegory, target: Actegory, obj_map: Dict[str, str], morph_map: Dict[str, str]):
    for src_obj, tgt_obj in obj_map.items():
        target.add_object(tgt_obj, source.objects[src_obj])
    
    for src_morph, tgt_morph in morph_map.items():
        target.add_morphism(tgt_morph, source.morphisms[src_morph])

def main():
    # Example usage
    act1 = Actegory("Actegory1")
    act1.add_object("A", 1)
    act1.add_object("B", 2)
    act1.add_morphism("f", lambda x: x + 1)
    act1.add_morphism("g", lambda x: x * 2)

    act2 = Actegory("Actegory2")
    actegory_functor(act1, act2, {"A": "X", "B": "Y"}, {"f": "h", "g": "k"})

    print(f"Actegory1 objects: {act1.objects}")
    print(f"Actegory1 morphisms: {list(act1.morphisms.keys())}")
    print(f"Actegory2 objects: {act2.objects}")
    print(f"Actegory2 morphisms: {list(act2.morphisms.keys())}")

    # Demonstrate composition
    composed = act1.compose("f", "g")
    print(f"Composition result: {composed(3)}")  # Should print 7 (f(g(3)) = (3*2)+1)

if __name__ == "__main__":
    main()
