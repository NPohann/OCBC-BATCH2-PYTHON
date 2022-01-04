// function Button () {
//     let value = 1
//     const name = 'Submit' //constant

//     function changeName() { // handler
//         // name = 'Send'
//         value  = 100
//     }

//     changeName()

//     console.log(value)

//     return 'done'
// }

// Button()



let numbers = [1,2,3,4,5]

let otherNumbers = [
    [
        [0,1],
        2,
        3
    ]
]

numbers.push(6)
numbers.unshift(0)

console.log(numbers)


// Arrow Function

// let a = 4;
// let b = 2;
// function () {
//     return a + b + 100;
// }

// let a = 4;
// let b = 2;
// () => a + b + 100;

// destructuring object

// const classroom = {
//     participants: ['Pieter', 'Esra', 'David', 'Alwi'],
//     session: 47,
//     name: 'FSD OCBC Batch 2'
// }

// const { participants, session, name } = classroom

// console.log(`
//     Halo ${name}!
//     Kita masuk ke dalam sesi ${session}.
//     Ada beberapa peserta: ${participants}
// `);

function getClassroom () {
    return {
        participants: ['Pieter', 'Esra', 'David', 'Alwi'],
        session: 47,
        name: 'FSD OCBC Batch 2'
    }
}

const { name, participants, session } = getClassroom()

console.log(`
    Halo ${name}!
    Kita masuk ke dalam sesi ${session}.
    Ada beberapa peserta: ${participants}
`);

const [ anto, budi ] = ['Budi', 'Anto']

console.log(budi, anto)