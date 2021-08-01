var grafico_MP, grafico_TEMP;

var MaterialParticulado = document.getElementById("G1").getContext("2d");;
var Temperatura = document.getElementById("G2").getContext("2d");;

const tiempo = 1000 * 10; 
var datos_mp = [
    {label: "MP 1.0 ug/m3",data: [], lineTension: 0.3, borderColor: 'Blue'},
    {label: "MP 2.5 ug/m3",data: [], lineTension: 0.3, borderColor: 'green'},
    {label: "MP 10 ug/m3",data: [], lineTension: 0.3, borderColor: 'red'}
];

var info_MP ={
    labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    datasets: [datos_mp[0], datos_mp[1], datos_mp[2]]
  };

var datosTemp = [
    { label: "Te", data: [] , borderColor: 'red'}
];

var info_TEMP = {
    labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
    datasets: [datosTemp[0]]
};
var chartOptions = {
    legend: {display: true, position: 'top', labels: {boxWidth: 80,fontColor: 'black'}}
};

function AlmacenaDatos(dData){
    datos_mp[0].data = dData[0];
    datos_mp[1].data = dData[1];
    datos_mp[2].data = dData[2];
    datosTemp[0].data = dData[3];
    info_TEMP.datasets = [datosTemp[0]]; 
    info_MP.datasets = [datos_mp[0],datos_mp[1],datos_mp[2]];
    graficar_MP();
    graficar_Temperatura();
};

function GetJson(){
    $.getJSON("http://127.0.0.1:5000/Get_Data", function(data){
        AlmacenaDatos(data);
    });
};

function graficar_MP() {
    grafico_MP = new Chart(MaterialParticulado, {
        type: 'spline',
        data: info_MP,
        options: chartOptions
    });
    grafico_MP.render();
};

function graficar_Temperatura(){
    grafico_TEMP = new Chart(Temperatura, {
        type: 'spline',
        data: info_TEMP,
        options: chartOptions
    });
    grafico_TEMP.render();
};

function Sample() {
    GetJson();
    grafico_MP.render();
    grafico_TEMP.render();
    graficar_MP();
    graficar_Temperatura();
};

graficar_MP();
graficar_Temperatura();
setInterval(Sample, tiempo);