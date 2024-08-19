window.onload = function() {
    function parseUrlAndSendPostRequest() {
        const currentUrl = window.location.href;

        // Проверка наличия access_token в фрагменте URL (после #)
        if (currentUrl.includes('#')) {
            const fragment = currentUrl.split('#')[1]; // Извлекаем часть после #
            const params = new URLSearchParams(fragment);
            const accessToken = params.get('access_token');
            const tokenType = params.get('token_type');
            const expiresIn = params.get('expires_in');
            const cid = params.get('cid');

            // Проверяем, что все необходимые параметры присутствуют
            if (accessToken && tokenType && expiresIn && cid) {
                // Формируем JSON для отправки
                const data = {
                    access_token: accessToken,
                    token_type: tokenType,
                    expires_in: expiresIn,
                    cid: cid
                };

                // Делаем POST запрос
                fetch('https://12fc-195-18-18-233.ngrok-free.app/save_yandex_data', {  // Замените на ваш URL
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    // Если запрос успешен, скрываем анимацию загрузки и показываем успех
                    document.getElementById('loader-container').style.display = 'none';
                    document.getElementById('success-container').style.display = 'block';
                })
                .catch(error => {
                    console.error('Ошибка при отправке данных:', error);
                });
            } else {
                console.error('Не найдены все необходимые параметры в URL');
            }
        } else {
            // Проверяем снова через 1 секунду
            setTimeout(parseUrlAndSendPostRequest, 1000);
        }
    }

    // Начинаем проверку сразу после загрузки страницы
    parseUrlAndSendPostRequest();
};
