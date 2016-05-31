var APP = {
	
	inizializza: function() {
		APP.init_daiRispettivoAlunno_click();
		APP.init_aggiungiAlunno_click();
	},

	init_daiRispettivoAlunno_click: function () {
		elementoSelezionato = $('#bottoneRichiestaAlunno');
		elementoSelezionato.on('click', function () {
			elementoChiaveRegistro = $("#campoTextChiaveRegistro");
			chiaveRegistro = elementoChiaveRegistro.val();
			$.ajax({
				method: "POST",
				url : "/alunnoByNumeroReg/",
				contentType: 'application/json',
				crossDomain: true,
				type: "json",
				data: JSON.stringify({numeroReg : chiaveRegistro}),
				dataType : "json",
				success : function (data){
					contenutoOutput = data.numeroReg + " " +
					data.nome + " " +
					data.cognome + " " +
					data.annoNascita;
					elementoOutput = $("#textOutput");
					elementoOutput.html(contenutoOutput)
				},
				error : function (result) {
					elementoOutput = $("#textOutput");
					elementoOutput.html("errore");
				} 
			});
		});
	},
	
	init_aggiungiAlunno_click: function() {
		elementoSelezionato = $('#bottoneRegistrazione');
		elementoSelezionato.on('click', function () {
			el1 = $("#campoTextNumReg");
            numeroReg = el1.val();
            el2 = $("#campoTextNome");
            nome = el2.val();
            el3 = $("#campoTextCognome");
            cognome = el3.val();
            el4 = $("#campoTextAnnoNascita");
            annoNascita = el4.val();
			$.ajax({
				method: "POST",
				url: "/inserisciAlunnoPOST/",
				contentType: 'application/json',
				crossDomain: true,
				type: "json",
				data: JSON.stringify({numeroReg: numeroReg, nome: nome, cognome: cognome, annoNascita: annoNascita}),
				dataType: "json",
				success: function(result) {
					alert("ok");
				},
				error: function() {
					alert("errore");
				}
			});
		});
	}
};

$(document).ready(function () {
	APP.inizializza();
});