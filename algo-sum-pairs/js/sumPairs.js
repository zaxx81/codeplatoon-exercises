exports.sumPairs = function(arr, num) {
    let len = arr.length
    let results = []
    let output = []
    
    for(let i = 0; i < len; i++) {
        for(let j = 0; j < len; j++) {
            if (i !== j) {
                let pairSum = arr[i] + arr[j]
                if (pairSum === num) {
                    let pairArr = [arr[i],arr[j]].sort(function(a, b){return a-b})
                    results.push (String(pairArr))

                }
            }
        }
    }
    
    let noDupes = [...new Set(results)]
    noDupes.map(elem => {
        let myNums = []
        myNums = elem.split(",")
        myNums[0] = Number(myNums[0])
        myNums[1] = Number(myNums[1])
        output.push(myNums)
    })

    if (output.length === 0) {
        return "unable to find pairs"
    }
    return output
}