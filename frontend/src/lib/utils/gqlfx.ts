// humanize a string
export function handleGqlErr(error:any):any {
    let errList:string[]=[];
    errList = errList.concat(error);
    console.log("graphQLErrors:", errList);
    if(errList.length > 0){
        return errList[0];
    }

    return "";
}
