const form = document.getElementById('user-form');
const input_H = document.getElementById('H');
const input_W = document.getElementById('W');
const input_l = document.getElementById('l');
const input_h = document.getElementById('h');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); 
    const userData = {
        H: Number(input_H.value),
        W: Number(input_W.value),
        h: Number(input_h.value),
        l: Number(input_l.value)
    };
    let {H, W, h, l} = userData;
    console.log(userData);
    if (H >= W){
        alert('Некорректный ввод! Сохраните пропорции H < W');
        return H;
    }
    
    if (l*2 >= W) {
        alert('Некорректный ввод! Главная ось l должна быть меньше W');
        return;
    }
    
    if (h*2 >= H) {
        alert('Некорректный ввод! Побочная ось h не может быть равна и более высоты H');
        return;
    } 

    let response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(userData)
        });
    let data = await response.json();
    if (response.ok) 
    {
        console.log(data, 'data from response');
        form.reset()
    }
    else if (response.status === 400) 
    {
        alert('Введены некорректные данные!')
        alert(data.message)
        console.log(data)
    }
    else 
    {
        alert('Ошибка сервера')
    }

});