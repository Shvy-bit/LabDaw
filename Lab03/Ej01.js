function NombreDia() {
    const Dia = document.getElementById("Dia").value;
    const resultado = document.getElementById("Resultado");
    let nombreDia = "";
    const dias = [
        "Domingo",
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado"
    ];
    if (Dia < 0 || Dia > 6) nombreDia = "Número de día inválido";
    else nombreDia = "El día es: " + dias[Dia];
    resultado.textContent = nombreDia;
}