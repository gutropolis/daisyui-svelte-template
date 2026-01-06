export const getStatusColor = (status: string) => {
		switch (status) {
			case 'Draft':
				return 'badge-warning';
			case 'Staging':
				return 'badge-info';
			case 'Production':
				return 'badge-success';
			default:
				return 'badge-gray';
		}
	};

export const getStatusIcon = (status: string) => {
		switch (status) {
			case 'Complete':
				return 'fa-check-circle text-green-600';
			case 'Incomplete':
				return 'fa-exclamation-circle text-yellow-600';
			case 'Unverified':
				return 'fa-question-circle text-blue-600';
			case 'Draft':
				return 'fa-pen-square text-gray-600';
			default:
				return 'fa-circle text-gray-600';
		}
	};