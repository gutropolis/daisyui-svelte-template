import Quill from 'quill'
// import {Delta} from 'quill/core.js'

export function quill(node, data, options) {
	const {plainclipboard = false, ...restOptions} = options

	const toolbar = [
		[{header: 1}, {header: 2}],
		['bold', 'italic', 'underline'],
		[{list: 'ordered'}, {list: 'bullet'}],
		['link', 'image', 'video'],
		['code-block', 'clean'],
	]

	 

	const q = new Quill(node, {
		modules: {
			toolbar,
			// history,
		},
		placeholder: 'Body',
		...restOptions,
	})

	if (plainclipboard === true) {
		q.clipboard.addMatcher(Node.ELEMENT_NODE, n => {
			const text = n.textContent
			// return new Delta().insert(text)
			return text
		})
	}

	const onTextChange = () => {
		const customEvent = new CustomEvent('text-change', {
			detail: {
				html: q.getSemanticHTML(),
				text: q.getText(),
			},
		})
		node.dispatchEvent(customEvent)
	}

	q.on('text-change', onTextChange)

	 
	q.clipboard.dangerouslyPasteHTML(data, 'api')

	return () => {
		q.off('text-change', onTextChange)
	}
}
