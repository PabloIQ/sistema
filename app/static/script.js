
function info(id){

    fetch(`/caso-detalle/${id}`, {
        headers:{
            'X-Requested-With': 'XMLHttpRequest'
        }
    }).then(
        function(response) {
            return response.json()
        }
    ).then(
        function(data) {
            console.log(data.desc)
            Swal.fire({
                icon: 'info',
                title: 'Detalles del caso',
                html: `
                    <p>
                        <b>ID:</b> ${id}
                    </p>
                    <p>
                        <b>Descripcion:</b> ${data.desc}
                    </p>
                    <p>
                        <b>Dispositivo:</b> ${data.dispositivo}
                    </p>
                    <p>
                        <b>Marca:</b> ${data.marca}
                    </p>
                    <p>
                        <b>Modelo:</b> ${data.modelo}
                    </p>
                    <p>
                        <b>Caso:</b> ${data.caso}
                    </p>
                `
              })
        }
    )
}