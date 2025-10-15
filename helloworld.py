"""Pequeño script de ejemplo: suma dos enteros.

Funciona de dos formas:
- Ejecutando interactivo: solicita dos números por teclado.
- Pasando dos argumentos desde la línea de comandos: `python helloworld.py 3 4`.

El script maneja entradas inválidas y muestra mensajes de ayuda.
"""

from __future__ import annotations
import sys


def parse_int(value: str) -> int:
	try:
		return int(value)
	except ValueError:
		raise ValueError(f"Valor no entero: {value!r}")


def main(argv: list[str] | None = None) -> int:
	argv = list(argv if argv is not None else sys.argv[1:])

	if len(argv) >= 2:
		# modo no interactivo: tomar los dos primeros argumentos
		try:
			a = parse_int(argv[0])
			b = parse_int(argv[1])
		except ValueError as exc:
			print(exc)
			return 2
	else:
		print("Hello world!")
		# modo interactivo: solicitar al usuario
		try:
			a = parse_int(input("Introduce el primer entero: "))
			b = parse_int(input("Introduce el segundo entero: "))
		except ValueError as exc:
			print(exc)
			return 2
		except (KeyboardInterrupt, EOFError):
			print("\nEntrada cancelada.")
			return 1

	print(f"Resultado: {a} + {b} = {a + b}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
