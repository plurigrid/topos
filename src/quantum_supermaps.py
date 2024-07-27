from typing import List, Tuple, Callable
import random

def lexical_diffusion(word: str, rate: float = 0.1) -> str:
    """Simulate lexical diffusion on a word."""
    return ''.join(c if random.random() > rate else random.choice('abcdefghijklmnopqrstuvwxyz') for c in word)

def equivariant_supermap(f: Callable[[str], str]) -> Callable[[List[str]], List[str]]:
    """Create an equivariant supermap from a given function."""
    return lambda words: [f(word) for word in words]

def mutual_recursion_a(n: int, words: List[str]) -> Tuple[int, List[str]]:
    """Mutual recursion function A."""
    if n <= 0:
        return (n, words)
    diffused = equivariant_supermap(lexical_diffusion)(words)
    return mutual_recursion_b(n - 1, diffused)

def mutual_recursion_b(n: int, words: List[str]) -> Tuple[int, List[str]]:
    """Mutual recursion function B."""
    if n <= 0:
        return (n, words)
    reversed_words = [word[::-1] for word in words]
    return mutual_recursion_a(n - 1, reversed_words)

def reflexivity_test(words: List[str]) -> bool:
    """Test reflexivity property."""
    supermap = equivariant_supermap(lambda x: x)
    return supermap(words) == words

def transitivity_test(words: List[str]) -> bool:
    """Test transitivity property."""
    supermap1 = equivariant_supermap(lexical_diffusion)
    supermap2 = equivariant_supermap(lambda x: x[::-1])
    supermap3 = equivariant_supermap(lambda x: supermap2(supermap1([x]))[0])
    return all(w1 == w2 for w1, w2 in zip(supermap3(words), supermap2(supermap1(words))))

def transclusion_test(words: List[str], subwords: List[str]) -> bool:
    """Test transclusion property."""
    supermap = equivariant_supermap(lexical_diffusion)
    transcluded = supermap(words + subwords)
    return all(word in transcluded for word in supermap(subwords))

def run_tests():
    words = ["quantum", "supermap", "equivariant", "lexical", "diffusion"]
    print("Initial words:", words)
    
    print("\nTesting mutual recursion:")
    result = mutual_recursion_a(5, words)
    print("Result after mutual recursion:", result)
    
    print("\nTesting reflexivity:")
    print("Reflexivity holds:", reflexivity_test(words))
    
    print("\nTesting transitivity:")
    print("Transitivity holds:", transitivity_test(words))
    
    print("\nTesting transclusion:")
    subwords = ["sub", "words"]
    print("Subwords:", subwords)
    print("Transclusion holds:", transclusion_test(words, subwords))

if __name__ == "__main__":
    run_tests()
