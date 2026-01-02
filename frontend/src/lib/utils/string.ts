// humanize a string
export function humanize(str: string) {
	return str
		.replace(/^[\s_]+|[\s_]+$/g, '')
		.replace(/[_\s]+/g, ' ')
		.replace(/^[a-z]/, function(m) {
			return m.toUpperCase();
		});
}

export function subStrWithDot(txt: string, from: number, length: number) {
	if (txt === '' || txt === undefined) {
		return '';
	}
	if (txt.length > length) {
		txt = txt.substring(from, length) + '...';
	}
	return txt;
}
export function subStrWithOutDot(txt: string, from: number, length: number) {
	if (txt === '' || txt === undefined) {
		return '';
	}
	if (txt.length > length) {
		txt = txt.substring(from, length) ;
	}
	return txt;
}


export function camelize(text: string) {
	const a = text.toLowerCase()
		.replace(/[-_\s.]+(.)?/g, (_, c) => c ? c.toUpperCase() : '');
	return a.substring(0, 1).toLowerCase() + a.substring(1);
} 
export function camelizeUnderScore(inputText: string): string {
    // Replace spaces with underscores and convert to uppercase
    const formattedText = inputText.replace(/\s+/g, '_').toUpperCase();

    // Remove non-alphanumeric characters
    const alphanumericText = formattedText.replace(/[^a-zA-Z0-9_]/g, '');

    return alphanumericText;
}
export function join(modalities:any) {
	const modalityJson = [].concat(modalities);
	if (modalityJson.length === 1) return modalityJson[0];
	return `${modalityJson.slice(0, -1).join(', ')} and ${modalityJson[modalityJson.length - 1]}`;
}


export function strWithUnderscore(text:string ){
		const newText = text.replaceAll(' ', '_');
		return newText.toLowerCase() ;
}
export function columnToExcelLetter(column:any):string
{
	let  temp, letter = '';
	while (column > 0)
	{
		temp = (column - 1) % 26;
		letter = String.fromCharCode(temp + 65) + letter;
		column = (column - temp - 1) / 26;
	}
	return letter;
}

// Utility function to trigger a browser download
export function DownloadFileByAchor(url, fileName) {
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName || 'download';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

