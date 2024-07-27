import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt
from lambeq import BobcatParser, AtomicType, IQPAnsatz, MPSAnsatz, remove_cups, rewrite_to_normal_form
from lambeq import Dataset, Model, Trainer
import torch

def ripser_analysis(data):
    """
    Perform topological data analysis using Ripser.
    
    This function is best for:
    - Analyzing the shape and structure of data
    - Detecting topological features like loops and voids
    - Computing persistent homology
    """
    result = ripser(data)
    plot_diagrams(result['dgms'], show=True)
    return result

def lambeq_sentence_classification(sentences, labels):
    """
    Perform sentence classification using lambeq.
    
    This function is best for:
    - Natural language processing tasks
    - Quantum-inspired sentence classification
    - Analyzing semantic structure of text
    """
    parser = BobcatParser()
    diagrams = [parser.parse(sentence) for sentence in sentences]
    diagrams = [remove_cups(d) for d in diagrams]
    diagrams = [rewrite_to_normal_form(d) for d in diagrams]
    
    ansatz = IQPAnsatz({AtomicType.NOUN: 1, AtomicType.SENTENCE: 1}, n_layers=1)
    circuits = [ansatz(d) for d in diagrams]
    
    dataset = Dataset(circuits, labels)
    model = Model(circuits[0], n_classes=len(set(labels)))
    
    trainer = Trainer(model, loss_function=torch.nn.CrossEntropyLoss())
    trainer.train(dataset, epochs=10, batch_size=2, lr=0.01)
    
    return model

def main():
    # Example usage of Ripser
    data = np.random.random((100, 2))
    ripser_result = ripser_analysis(data)
    print("Ripser analysis complete. Check the plot for persistent homology diagram.")

    # Example usage of lambeq
    sentences = ["The cat sat on the mat", "The dog ran in the park"]
    labels = [0, 1]
    lambeq_model = lambeq_sentence_classification(sentences, labels)
    print("lambeq sentence classification model trained.")

if __name__ == "__main__":
    main()
