from parser import Parser
from evaluador import Evaluator

def main():
    evaluador = Evaluator()

    with open("entrada.txt", "r") as f:
        lineas = f.readlines()

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue

        parser = Parser(linea)
        tree = parser.parse()
        resultado = evaluador.visit(tree)

        print(f"{linea} = {resultado}")

if __name__ == "__main__":
    main()
