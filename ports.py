import subprocess

def abrir_puerto(ip_interna, puerto, protocolo):
    try:
        result = subprocess.run(
            ["upnpc", "-e", f"Port {puerto}", "-a", ip_interna, str(puerto), str(puerto), protocolo],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Puerto {puerto} ({protocolo}) abierto correctamente en la IP interna {ip_interna}.")
    except subprocess.CalledProcessError as e:
        print(f"Error al abrir el puerto {puerto} ({protocolo}) en la IP interna {ip_interna}.\n{e.stderr}")

def cerrar_puerto(puerto, protocolo):
    try:
        result = subprocess.run(
            ["upnpc", "-d", str(puerto), protocolo],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Puerto {puerto} ({protocolo}) cerrado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al cerrar el puerto {puerto} ({protocolo}).\n{e.stderr}")

def main():
    print("[1] Abrir")
    print("[2] Cerrar")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        accion = "abrir"
    elif opcion == "2":
        accion = "cerrar"
    else:
        print("Opción no válida. Por favor elige 1 o 2.")
        return

    ip_interna = input("Introduce la IP interna: ")
    puerto = input("Introduce el puerto: ")
    protocolo = input("Introduce el protocolo (tcp/udp): ")

    if accion == "abrir":
        abrir_puerto(ip_interna, puerto, protocolo)
    elif accion == "cerrar":
        cerrar_puerto(puerto, protocolo)

if __name__ == "__main__":
    main()
