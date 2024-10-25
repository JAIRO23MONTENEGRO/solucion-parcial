BONIFICACION_DIRECTIVO_ALTO=0.20
BONIFICACION_DIRECTIVO_MEDIO=0.10
BONIFICACION_OPERATIVO_ALTO=0.15
BONIFICACION_OPERATIVO_MEDIO=0.05

def calcular_bonificacion(cargo, desempeno, salario_base):

    if cargo=="directivo":
        if desempeno=="alto":
            bonificacion= salario_base * BONIFICACION_DIRECTIVO_ALTO
        elif desempeno == "mediio":
            bonificacion= salario_base * BONIFICACION_DIRECTIVO_MEDIO
        else:
            bonificacion =0
    elif cargo == "operativo":
        if desempeno=="alto":
            bonificacion= salario_base * BONIFICACION_OPERATIVO_ALTO
        elif desempeno == "mediio":
            bonificacion= salario_base * BONIFICACION_OPERATIVO_MEDIO
        else:
            bonificacion =0
    else:
      bonificacion=0
    return bonificacion

#Segunda funcion
def calcular_total(salario_base, bonificacion):
    return salario_base + bonificacion

def imprimir_resumen(cargo,desempeno,salario_base, bonificacion,total):
    print("------Resumen del Pago------")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de desempeño : {desempeno.capitalize()}")
    print(f"Salario Base : ${salario_base}")
    print(f"Bonificación : ${bonificacion}")
    print(f"Total a Recibir: ${total}")
    print("---------------------------")

salario_base = float(input("Ingrese el salario base mensual: $"))
cargo = input("Ingrese el cargo del empleado (directivo/operativo):").lower()
desempeno = input("Ingrese el nivel de desempeño (alto/medio/bajo):").lower()

#calcular bonificacion
bonificacion =calcular_bonificacion(cargo,desempeno,salario_base)

#calcular total a recibir
total=calcular_total(salario_base,bonificacion)

#Invocamos la funcion
imprimir_resumen(cargo,desempeno,salario_base,bonificacion,total)

