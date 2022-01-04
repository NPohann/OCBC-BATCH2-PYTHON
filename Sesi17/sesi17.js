// CALLBACK 

// function display (value) {
//     console.log(value)
// }

// function calculator(number1, number2, callback){
//     const result = number1 + number2
//     callback(result)
// }

// const displayVar = function(value){
//     console.log(value)
// }

// // calculator(10, 15, function(value){ // function expression
// //     console.log(value)
// // })

// calculator(10, 15, displayVar)

// PROMISE

function buatJanji(message) {
    return new Promise((resolve, reject) => {
        if(message == "") return reject('Isi janji harus diisi')

        return resolve('Berhasil ditepati')
    })
}
