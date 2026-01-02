/* Copyright (c) 2022. Ankit Patial.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Ankit Patial
 */

/**
 * Function to sleep a thread for sometime
 */
export default function sleep(ms) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}
