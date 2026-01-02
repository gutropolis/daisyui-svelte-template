/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

export function copyToClipboard(input) {
	return () => {
		if (!navigator?.clipboard) return;

		input.select();
		input.setSelectionRange(0, 99999); // For mobile devices
		navigator.clipboard.writeText(input.value);
	};
}
