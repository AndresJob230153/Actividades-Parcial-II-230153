def validar_ip(ip):
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:

        if not parte.isdigit():
            return False

        numero = int(parte)

        if numero < 0 or numero > 255:
            return False

    return True