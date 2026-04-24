function Ej01() {
    const Dia = document.getElementById("Dia").value;
    const resultado = document.getElementById("Resultado01");
    let nombreDia = "";
    const dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"];
    if (Dia < 0 || Dia > 6) nombreDia = "Número de día inválido";
    else nombreDia = "El día es: " + dias[Dia];
    resultado.textContent = nombreDia;
}
function Ej02() {
    const Text = document.getElementById("Text").value;
    const resultado = document.getElementById("Resultado02");
    let textInvertido = "";
    for (let i = Text.length - 1; i >= 0; i--) {
        textInvertido += Text[i];
    }
    resultado.textContent = "Texto invertido: " + textInvertido;
}
function Ej03() {
    const resultado = document.getElementById("Resultado03");
    const hoy = new Date();
    const diaArequipa = new Date(hoy.getFullYear(), 8, 15);
    const diferencia = Math.ceil((diaArequipa - hoy) / (1000 * 60 * 60 * 24));
    resultado.textContent = "Faltan: " + diferencia + " días";
}function Ej04() {
    const codigo = document.getElementById("Codigo").value;
    const resultado = document.getElementById("Resultado04");
    let cd = "";
    // Verifica si la url empieza con https://meet.google.com/ y que qkj-uksn-nbc pase a qkjuksnnbc
    if (codigo.startsWith("https://meet.google.com/")) {
        const partes = codigo.split("/");
        if (partes.length === 4) {
            const codigoReunion = partes[3].replace(/-/g, "");
            cd = "Código de reunión: " + codigoReunion;
        }
    }
    else cd = "URL inválida";
    resultado.textContent = cd;
}